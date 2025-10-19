```json
{
  "id": "7a9ebc12ec8c554d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291221,
  "host_pid": "9e6742732c60:1",
  "hash": "8999f30f4ba762d20244a8f6d98e383d5e1b226da6560c76c47fbdad8ed6bd4a",
  "cid": "QmV18999f30f4ba762d20244a8f6d98e383d5e1b226d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291221,
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
      "evaluated_at": 1760291221
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
  "sig": "1c295ffca72e4cde986a3c857980f2012a1cf36108abbc15246a8f0a85b82741"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}