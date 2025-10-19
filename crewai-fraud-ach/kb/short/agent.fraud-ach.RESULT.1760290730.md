```json
{
  "id": "1394a7575aadb431",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290730,
  "host_pid": "9e6742732c60:1",
  "hash": "852c5098bcf5daa3e47ca0885bc9f1bfdbbd9f8d69bfab46d940562627a82775",
  "cid": "QmV1852c5098bcf5daa3e47ca0885bc9f1bfdbbd9f8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290730,
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
      "evaluated_at": 1760290730
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
  "sig": "5a225761740eb9d789095728625287ae9a8082189ad771e2b0c6e240c2b29a24"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 68114432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}