```json
{
  "id": "3fe88b81c16ce24b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292274,
  "host_pid": "9e6742732c60:1",
  "hash": "df7adaa20458991ad409275b589d9bef3c637221f1448c54d0eb86cc93f591c1",
  "cid": "QmV1df7adaa20458991ad409275b589d9bef3c637221",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292274,
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
      "evaluated_at": 1760292274
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
  "sig": "1ccdd68ff1a8287aca334b7e5c6fde5c4f070f7e7791ecc64df3c569a15e16eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028364021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'f023f2061dd68ffa'}}}een': 1760285763, 'matching_hash': '62b45bc192f4101a'}}}