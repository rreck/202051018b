```json
{
  "id": "c069116d2dc4ae85",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293097,
  "host_pid": "9e6742732c60:1",
  "hash": "fedc3a930c468104a317fe6e85f10a54fad01cdba423f402d4e83b8b67797d99",
  "cid": "QmV1fedc3a930c468104a317fe6e85f10a54fad01cdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293097,
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
      "evaluated_at": 1760293097
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
  "sig": "dd35b1bc097fdd6d6b94458fc0b151a873114265db76ab1fe5687cf47da0420e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 10550000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}