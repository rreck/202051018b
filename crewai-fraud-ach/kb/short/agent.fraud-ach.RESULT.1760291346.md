```json
{
  "id": "bb5afb45988a236d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291346,
  "host_pid": "9e6742732c60:1",
  "hash": "3585d672261ef174631d4ae73b67b1c739173cf1f96a1100bf6852edf5365af8",
  "cid": "QmV13585d672261ef174631d4ae73b67b1c739173cf1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291346,
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
      "evaluated_at": 1760291346
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
  "sig": "417b832601809cc257d9635bb15fca70729621014645d63798f86830bafbf77d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460208894
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 83184455, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '36d88bd4e0ec214b'}}}