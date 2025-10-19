```json
{
  "id": "1a3897294fd82b74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289973,
  "host_pid": "9e6742732c60:1",
  "hash": "9789fdda2864d6913bd404c078f544e913bd0cdb96cf445f0c51366f0f822812",
  "cid": "QmV19789fdda2864d6913bd404c078f544e913bd0cdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289973,
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
      "evaluated_at": 1760289973
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
  "sig": "7b06d12e7b9eb94a1eedca5994435f14aed99c633e075ed9f8286ed2d214c54d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245035140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 55894830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'af29b59576821758'}}}