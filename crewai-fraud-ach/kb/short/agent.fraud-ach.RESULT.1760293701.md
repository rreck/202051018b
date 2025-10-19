```json
{
  "id": "f8b40ec157274bf7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293701,
  "host_pid": "9e6742732c60:1",
  "hash": "1e4aec2dc8c94e8b49e806e950ae2d41d30010a8acbc4f1286747a3cb2c9136d",
  "cid": "QmV11e4aec2dc8c94e8b49e806e950ae2d41d30010a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293701,
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
      "evaluated_at": 1760293701
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
  "sig": "3c4194743a8368cf5112e3c05474821b26fdf6a6feb9719d31408808a209bb41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 30648800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}