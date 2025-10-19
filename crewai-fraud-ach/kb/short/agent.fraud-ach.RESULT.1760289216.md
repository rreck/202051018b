```json
{
  "id": "242e6f248e773261",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289216,
  "host_pid": "9e6742732c60:1",
  "hash": "c5eda1531043b62eb381c33546c559e0c089e33015bafdc3c1965506fdfde73d",
  "cid": "QmV1c5eda1531043b62eb381c33546c559e0c089e330",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289216,
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
      "evaluated_at": 1760289216
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
  "sig": "47162572b374adb8a1f57d39d2e4562276e5863091ad2155cc54e67a6ed11a4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278201542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 34434855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'ee525b8c336c7bb1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}