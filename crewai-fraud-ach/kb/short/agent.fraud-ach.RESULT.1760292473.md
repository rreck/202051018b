```json
{
  "id": "c9527a6dbacbfc2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292473,
  "host_pid": "9e6742732c60:1",
  "hash": "ef41e52aa9588aa0ee20bd493c255a2bdc1cf2d17a5be9f74712e48794c242db",
  "cid": "QmV1ef41e52aa9588aa0ee20bd493c255a2bdc1cf2d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292473,
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
      "evaluated_at": 1760292473
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
  "sig": "c34ede0696442b758913cc58e7864d67e795f83fe0fca455b66ad07fee4bc527"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021005824
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}