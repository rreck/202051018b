```json
{
  "id": "1a5be5c78ff783c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290628,
  "host_pid": "9e6742732c60:1",
  "hash": "8c82b631ad6ff3ba930faf899acfd7d06422ee28fe267e25d62e29986720b437",
  "cid": "QmV18c82b631ad6ff3ba930faf899acfd7d06422ee28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290628,
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
      "evaluated_at": 1760290628
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
  "sig": "bd78d02014cf216b7d389212055acf85015af8e9457de1e2720eda5156f7ce17"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244838202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 55460790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}