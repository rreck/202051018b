```json
{
  "id": "b6888f066de20897",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293668,
  "host_pid": "9e6742732c60:1",
  "hash": "e412301cd964f19e57b1b1c7061665dfc54624ae2eba1b3cde5a0e119ae392ec",
  "cid": "QmV1e412301cd964f19e57b1b1c7061665dfc54624ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293668,
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
      "evaluated_at": 1760293668
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
  "sig": "4a5931588fd30abb0467e1d675a16c9949fc38d6e9883fad9b1205c593bd0c96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240708140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 23797891, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'e22b1a9baac54cae'}}}