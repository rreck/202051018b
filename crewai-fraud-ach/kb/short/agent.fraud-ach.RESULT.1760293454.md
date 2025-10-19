```json
{
  "id": "3e8415ca8463411a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293454,
  "host_pid": "9e6742732c60:1",
  "hash": "100904891e81bebad343f2663ae3baf779b39ee36379d99427d1c944d2284189",
  "cid": "QmV1100904891e81bebad343f2663ae3baf779b39ee3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293454,
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
      "evaluated_at": 1760293454
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
  "sig": "664d68481770b64ae7776ac54f99de23c2dd48a0f915bfaa5a38524edd8c5bae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152477967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 74536869, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '1f16fe6ce32cfab1'}}}