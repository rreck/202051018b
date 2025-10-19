```json
{
  "id": "37e995715374ad6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287884,
  "host_pid": "9e6742732c60:1",
  "hash": "03591bedb08e1c992f3819d132b3f6c88a4cd9e8c63170d49f1443e6827dd825",
  "cid": "QmV103591bedb08e1c992f3819d132b3f6c88a4cd9e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287884,
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
      "evaluated_at": 1760287884
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "218c510887f2ca3a594801f788f1e1e1c1c50aa2f71f84566b6c5f61ad04ae5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 23868600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}