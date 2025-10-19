```json
{
  "id": "2fc46643e990de1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290238,
  "host_pid": "9e6742732c60:1",
  "hash": "57ad7b2922e72972101abf0b985c8ec6645d77eac246a5a69ebbb07360f06982",
  "cid": "QmV157ad7b2922e72972101abf0b985c8ec6645d77ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290238,
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
      "evaluated_at": 1760290238
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
  "sig": "f9fb6892ce252582e593072430af27617cf236797f6734b44621d4b991e7dd87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028786297
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 48302255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'f6cfe00d30182bd5'}}}