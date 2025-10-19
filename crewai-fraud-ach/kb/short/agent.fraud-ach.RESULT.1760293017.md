```json
{
  "id": "96516bbf6955feb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293017,
  "host_pid": "9e6742732c60:1",
  "hash": "27eee2f1c18b80e04263f7d92d2cecfd51e1b01d7162a29d179094a8fc113351",
  "cid": "QmV127eee2f1c18b80e04263f7d92d2cecfd51e1b01d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293017,
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
      "evaluated_at": 1760293017
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
  "sig": "470812beff2265718b3b8aeb1a11f7ef4bd10a6507e54cd95d9fd331a62d6ec2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460168239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 17276490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'c8b812a49265f53e'}}}