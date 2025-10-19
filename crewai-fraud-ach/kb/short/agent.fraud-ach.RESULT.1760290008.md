```json
{
  "id": "1401ea53d8786709",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290008,
  "host_pid": "9e6742732c60:1",
  "hash": "1c7223ac2dc976228e77758f88a862c3200eb7395ccf1153d7c23a01eb397c21",
  "cid": "QmV11c7223ac2dc976228e77758f88a862c3200eb739",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290008,
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
      "evaluated_at": 1760290008
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
  "sig": "bd2efef33e456a8674748c105149ea7d32aefe97444713dc61e2b86cd98ebac4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244807015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 13900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': 'e3fbbc71f2accf8f'}}}