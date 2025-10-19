```json
{
  "id": "5c86a3909d16c864",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294556,
  "host_pid": "9e6742732c60:1",
  "hash": "add30e652d6ac35fff048bfd56cec17613ec8e186a74c98a1e3a5b4f7dd5027a",
  "cid": "QmV1add30e652d6ac35fff048bfd56cec17613ec8e18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294556,
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
      "evaluated_at": 1760294556
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
  "sig": "3a05323d480d85d96ec7ea47e3c71e4ea039605cb25557c748a575951c7a437e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 98332320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}}