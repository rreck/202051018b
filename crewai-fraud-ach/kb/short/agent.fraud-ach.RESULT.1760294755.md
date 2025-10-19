```json
{
  "id": "0200842e7b8ec0df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294755,
  "host_pid": "9e6742732c60:1",
  "hash": "761701d253d0449ea4b50787ee14963aad49ecc1939a46ed687832b3332e5474",
  "cid": "QmV1761701d253d0449ea4b50787ee14963aad49ecc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294755,
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
      "evaluated_at": 1760294755
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
  "sig": "69be3860e1b7bc1720491a989acf4098b592fe7b6cd339675275eba1578adace"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025380503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 19196944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '5a364e4e5c1e4dba'}}}