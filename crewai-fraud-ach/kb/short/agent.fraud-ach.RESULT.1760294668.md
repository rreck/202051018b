```json
{
  "id": "0db874b652a75631",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294668,
  "host_pid": "9e6742732c60:1",
  "hash": "7d7106308c877c63975d713cd6f5acc9185fa355f290860db4b70b49e4f87462",
  "cid": "QmV17d7106308c877c63975d713cd6f5acc9185fa355",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294668,
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
      "evaluated_at": 1760294668
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
  "sig": "955404c5cb8d34975c8f23aa622b3b549840dbb112844a25a4dbbde340e0a488"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596790322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 318, 'threshold': 50, 'total_amount': 16642212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 317, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}