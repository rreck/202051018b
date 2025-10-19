```json
{
  "id": "74cdb1b23374ee17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293308,
  "host_pid": "9e6742732c60:1",
  "hash": "3fb60e7b5509ae688523f0865e6020b0be76e5ab8c140c79d3c7ceda5968adf2",
  "cid": "QmV13fb60e7b5509ae688523f0865e6020b0be76e5ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293308,
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
      "evaluated_at": 1760293308
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
  "sig": "57cd69a55198b4df734c8b937ba53ed452e90b5aa4b305bfb2a7ee7f50d1ea37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277570300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 87366168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '94740eaab516570d'}}}