```json
{
  "id": "04da864d165e74cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291394,
  "host_pid": "9e6742732c60:1",
  "hash": "24198537aff32490b371552f805f2cc1486b23a03e915fb90e94e36f2c4a67e8",
  "cid": "QmV124198537aff32490b371552f805f2cc1486b23a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291394,
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
      "evaluated_at": 1760291395
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
  "sig": "b655b1a02c39b04db578ece4cc0bac3c268ba48eec67ba40d206df7c89550696"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038197650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 32723658, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '1b9150809eb731a5'}}}