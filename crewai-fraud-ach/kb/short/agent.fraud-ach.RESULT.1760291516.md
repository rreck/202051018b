```json
{
  "id": "0bceda770535b271",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291516,
  "host_pid": "9e6742732c60:1",
  "hash": "4f219041568fea8d5bb344c0fa7c15dd3c368b7c3856d8aa3354380881116094",
  "cid": "QmV14f219041568fea8d5bb344c0fa7c15dd3c368b7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291516,
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
      "evaluated_at": 1760291516
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
  "sig": "c0878d88c9b0c04c098291d54a32f939546eb62e3655fef26614da6176b095da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 76305408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}