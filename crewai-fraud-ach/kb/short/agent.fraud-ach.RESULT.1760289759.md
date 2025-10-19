```json
{
  "id": "322e1be2baa0be18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289759,
  "host_pid": "9e6742732c60:1",
  "hash": "3456e949cfe74ef3bddfd013727e52b3549148a074a86538b57c3d2bfa433c4b",
  "cid": "QmV13456e949cfe74ef3bddfd013727e52b3549148a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289759,
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
      "evaluated_at": 1760289759
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
  "sig": "32d0569da8ec92cb665d2f9c67fd4ac70cdaff0dbd615a699f1b77ad3156776a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466969713
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 41064408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '1e9180284a8352f5'}}}