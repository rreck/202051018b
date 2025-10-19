```json
{
  "id": "e2c73f55276139b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291012,
  "host_pid": "9e6742732c60:1",
  "hash": "50a3c7d7ad1b35d1ce01874351ee1fa772ae402afdfef74854b10b1794de68e9",
  "cid": "QmV150a3c7d7ad1b35d1ce01874351ee1fa772ae402a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291012,
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
      "evaluated_at": 1760291012
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "b1b8e45a8ecb18029ed8aa58355370def35aea36873442a8ecb1eb93663b1fae"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 530764332360017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 33769890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '09bd6f4aa98253cc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}