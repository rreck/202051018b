```json
{
  "id": "4d839fc840873eb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287732,
  "host_pid": "9e6742732c60:1",
  "hash": "1bd6a43289e8d73bf7082e4cd14d768dd3c7dabad418a3d831c9eaf4a263af42",
  "cid": "QmV11bd6a43289e8d73bf7082e4cd14d768dd3c7daba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287732,
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
      "evaluated_at": 1760287732
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
  "sig": "ed5bcb1978d1eec1e789519a7fa1dc6c79b85b8ff16871d2e8d23b8c7e23af50"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 23409960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}