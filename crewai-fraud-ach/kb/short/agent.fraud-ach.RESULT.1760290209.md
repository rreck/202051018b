```json
{
  "id": "bd9337aabf30a738",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290209,
  "host_pid": "9e6742732c60:1",
  "hash": "5086f113058c27f6af3f197a40368031557736c6eb2ff363b63c882123a504f3",
  "cid": "QmV15086f113058c27f6af3f197a40368031557736c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290209,
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
      "evaluated_at": 1760290209
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
  "sig": "139dc002668f39af518c445af41930d2fc641400148b4f746f4d2f06a3acb3f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592552790
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 47238480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': 'c5daecdc9bc16873'}}}