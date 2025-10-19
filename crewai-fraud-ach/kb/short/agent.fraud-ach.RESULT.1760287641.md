```json
{
  "id": "7903ae6fcc3dbc68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287641,
  "host_pid": "9e6742732c60:1",
  "hash": "9ee8bb2a61586d24179f92e7a6a55f9dcb6b454445670191f1388e7ad24ec8db",
  "cid": "QmV19ee8bb2a61586d24179f92e7a6a55f9dcb6b4544",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287641,
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
      "evaluated_at": 1760287641
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
  "sig": "723f33d7526c19cd29b085479779acc032b1e7a816636d541bc9818e09504514"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 29717113, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}