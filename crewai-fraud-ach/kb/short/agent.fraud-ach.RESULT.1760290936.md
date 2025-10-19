```json
{
  "id": "2c4eb0054c8e342b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290936,
  "host_pid": "9e6742732c60:1",
  "hash": "9256036fcacbd57c2640770dc5ece8fc5024f600b1551fe28cc3518e96201fe3",
  "cid": "QmV19256036fcacbd57c2640770dc5ece8fc5024f600",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290936,
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
      "evaluated_at": 1760290936
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
  "sig": "323836eb0467e80471e6d574bca162ed4a97cf317f039c838f38b8ed71fdcbaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033621272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 24310146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'd5b1a20ced8a5769'}}}