```json
{
  "id": "27e761c5b85f4bb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289929,
  "host_pid": "9e6742732c60:1",
  "hash": "ac94e9d8f0968dc0878bcd74cccc8bdbb0a82e274b883804d054d133f2c19fcb",
  "cid": "QmV1ac94e9d8f0968dc0878bcd74cccc8bdbb0a82e27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289929,
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
      "evaluated_at": 1760289929
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
  "sig": "e759215a374719b84dde61e366db4a6f44e9fae3fd9c65f00f9a5d7cde28917f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462075291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 43283643, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}