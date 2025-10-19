```json
{
  "id": "d6ae0cd42ade6a30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293714,
  "host_pid": "9e6742732c60:1",
  "hash": "fd6cc043f63d6336f4fa104f08d82d58bd63288b502ee02908c9ef182fb642af",
  "cid": "QmV1fd6cc043f63d6336f4fa104f08d82d58bd63288b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293714,
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
      "evaluated_at": 1760293714
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
  "sig": "f375316b8cb0c29071a4d6b148b8936e8da561c7c7aaca2cda7522b25422692e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460526260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 80046400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '4d7dea8b6c0fe79e'}}}