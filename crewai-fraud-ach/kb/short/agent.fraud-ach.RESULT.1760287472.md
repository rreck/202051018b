```json
{
  "id": "0d979d6874f2749b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287472,
  "host_pid": "9e6742732c60:1",
  "hash": "abdf2aba7486c00e46c409728d3d053a718f1439c9122d893e4bc604dfd67d29",
  "cid": "QmV1abdf2aba7486c00e46c409728d3d053a718f1439",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287472,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760287472
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "742236b45c627cd1e3e4bd1425cedc87c917beedc3d1916d7a98d5476cd355e1"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 111000020716291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 11534002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': 'a2f2d41c7f22f612'}}}