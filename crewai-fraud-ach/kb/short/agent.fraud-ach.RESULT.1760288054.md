```json
{
  "id": "fd07582f3af31208",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288054,
  "host_pid": "9e6742732c60:1",
  "hash": "0efd8b498677c682707cb9d7826d572a299e5c34b77988ce7cd716f49643068d",
  "cid": "QmV10efd8b498677c682707cb9d7826d572a299e5c34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288054,
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
      "evaluated_at": 1760288054
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
  "sig": "d5944af32f170e3d8ba570c0189c3def14e41172ff37ce9acff1078e11c0bdce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026466423
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 38250306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285764, 'matching_hash': '1fcdc28f16166b10'}}}