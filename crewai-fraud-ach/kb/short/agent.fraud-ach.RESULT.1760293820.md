```json
{
  "id": "368f7bc0afb2bf2b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293820,
  "host_pid": "9e6742732c60:1",
  "hash": "8c2ff2728a75f1269d7d2a3c123717b91d295bb3c829dd5b673c22d6fdd3b270",
  "cid": "QmV18c2ff2728a75f1269d7d2a3c123717b91d295bb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293820,
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
      "evaluated_at": 1760293820
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
  "sig": "e9c3a36d071a88a459981e9a00eb232f086e688ce1ff16acc4c9a9e46d04b887"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022401094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 92251618, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '4e5cfda15432477b'}}}