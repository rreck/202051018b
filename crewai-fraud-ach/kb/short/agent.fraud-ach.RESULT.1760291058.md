```json
{
  "id": "7e1011a3b70cfa98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291058,
  "host_pid": "9e6742732c60:1",
  "hash": "1fe1fbaeeacd984fb7c9fbd458829473f07d4ee922faad11724551fc6ae558e7",
  "cid": "QmV11fe1fbaeeacd984fb7c9fbd458829473f07d4ee9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291058,
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
      "evaluated_at": 1760291058
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
  "sig": "56c2c449ee0c856632b682c3a2206407353c24b742e0b507a9d3b82b653e6405"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245652457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 14116142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '6ac12dd8f1799493'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}