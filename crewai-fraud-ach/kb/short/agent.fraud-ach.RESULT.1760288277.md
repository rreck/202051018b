```json
{
  "id": "94c32b403f16e1a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288277,
  "host_pid": "9e6742732c60:1",
  "hash": "87059f4e2ac01322822071694484b26bf25d141db6a5f7dfbc5ac041d3b64161",
  "cid": "QmV187059f4e2ac01322822071694484b26bf25d141d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288277,
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
      "evaluated_at": 1760288277
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "bcdaffff2243d94f861bc253d816205ce4a583bbc8008470dab639b32c739b89"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105153391998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 683290608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285764, 'matching_hash': '05c5de8ca533802c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7764666}}}