```json
{
  "id": "fd3f5cdbe74a936c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289714,
  "host_pid": "9e6742732c60:1",
  "hash": "44de62ee072561079f7e36f44550b6f5ac76374134e07093a0c6fb90da2bd2df",
  "cid": "QmV144de62ee072561079f7e36f44550b6f5ac763741",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289714,
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
      "evaluated_at": 1760289714
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
  "sig": "756202c643b8727ded3eac600711a8a9fea383a4e8c0ac84867351d1f684aea9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032147418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 48609122, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': '7eb9a0fe320f28ac'}}}