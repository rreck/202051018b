```json
{
  "id": "8137c7d953302de9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294698,
  "host_pid": "9e6742732c60:1",
  "hash": "c9d49594b7b1975ad1c205c6f15c2f4b4c8ba9aa071cf798cbd2b937cd52a808",
  "cid": "QmV1c9d49594b7b1975ad1c205c6f15c2f4b4c8ba9aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294698,
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
      "evaluated_at": 1760294698
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
  "sig": "7c17e0bb7ac7d39f051bab48485bfad56435b622fda310dd80e756f0cbd625bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248569332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 36155241, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}