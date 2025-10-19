```json
{
  "id": "50bcdd65427f21b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291634,
  "host_pid": "9e6742732c60:1",
  "hash": "8cce20387893d759b6456dedf040846987bfd16a7c19f9f519a4eda461c3a1eb",
  "cid": "QmV18cce20387893d759b6456dedf040846987bfd16a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291634,
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
      "evaluated_at": 1760291634
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
  "sig": "7a5a3d41924a9e2e0f8821ce888d927ce196e59ed1d441bbe108239c0aee6b64"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 35257272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}