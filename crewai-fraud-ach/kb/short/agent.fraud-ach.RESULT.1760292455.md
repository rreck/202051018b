```json
{
  "id": "f3527d53e4b35772",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292455,
  "host_pid": "9e6742732c60:1",
  "hash": "6d1a5ed4e97544d00c1fbda200cf195c10eb26279e0bf2d29e2dde6feb8d9cee",
  "cid": "QmV16d1a5ed4e97544d00c1fbda200cf195c10eb2627",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292455,
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
      "evaluated_at": 1760292455
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
  "sig": "b1ba98f6e76110f27f16f9483cf906003e702df46f9627571ba3d2c797d48a7a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157835836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 87351264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '17512b782db0f875'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}