```json
{
  "id": "a669c4e6298c5cba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289964,
  "host_pid": "9e6742732c60:1",
  "hash": "53d60f810fd1f20b50d711516d225480d53fc6ff6ea5ad903e2fe591ef4b647b",
  "cid": "QmV153d60f810fd1f20b50d711516d225480d53fc6ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289964,
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
      "evaluated_at": 1760289964
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
  "sig": "d5ff14cfb4c6bd55e5744c1682c82c7dc39824b4ca1af75cd875243151865d56"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 40229484, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '12aaf4f6bb764c37'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}