```json
{
  "id": "08f301360150e7ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290852,
  "host_pid": "9e6742732c60:1",
  "hash": "331ce38848cd275f96fef968f0333e3466932d92510adc91bdf34eed7b9046fd",
  "cid": "QmV1331ce38848cd275f96fef968f0333e3466932d92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290852,
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
      "evaluated_at": 1760290852
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
  "sig": "665c204646287d529a7d6c76f4f53d8852410171e090ba6f2174fa06d733829d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465033668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 73276574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '0c3b43b3004009ec'}}}maly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9144651}}}