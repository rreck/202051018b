```json
{
  "id": "8326cb60a9193ab8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293787,
  "host_pid": "9e6742732c60:1",
  "hash": "24b18fc15fa97283ee1b9f48230b9ac76c6865383d1dbd02845e4e1e31d26f8f",
  "cid": "QmV124b18fc15fa97283ee1b9f48230b9ac76c686538",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293787,
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
      "evaluated_at": 1760293787
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
  "sig": "b4c789db07db9de3c6e4a771c23e8c81832540495a86c882bbad2653ac553d06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 94034700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': 'adb809538e6eb6af'}}}