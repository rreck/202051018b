```json
{
  "id": "f95e6c34b97b0a4e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292242,
  "host_pid": "9e6742732c60:1",
  "hash": "1252a0956ed435ec92fb194d1f4e2ac74678bfd68a32c9e9eb3adc28e263e2ee",
  "cid": "QmV11252a0956ed435ec92fb194d1f4e2ac74678bfd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292242,
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
      "evaluated_at": 1760292242
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
  "sig": "490c58c90d05b27b768f306efa2df5fa9da0dbf096798f419d005e83b20e274b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466969713
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 60041142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '1e9180284a8352f5'}}}