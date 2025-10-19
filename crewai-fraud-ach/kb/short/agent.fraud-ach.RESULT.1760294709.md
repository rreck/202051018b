```json
{
  "id": "1972b7f884a0f8b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294709,
  "host_pid": "9e6742732c60:1",
  "hash": "89a31cbc566ea51f236263bff52f2d8ce081996649dbbc031e0658834a635f47",
  "cid": "QmV189a31cbc566ea51f236263bff52f2d8ce0819966",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294709,
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
      "evaluated_at": 1760294709
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
  "sig": "c4d006e3c1e6bbaa9570fe7c3b333ad79b6ff3bd170842da88e7833be590e45c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591790243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 17066619, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '8c245acd6e70ddc0'}}}