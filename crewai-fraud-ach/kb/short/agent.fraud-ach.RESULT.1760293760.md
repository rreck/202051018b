```json
{
  "id": "4c56eb09c26c8283",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293760,
  "host_pid": "9e6742732c60:1",
  "hash": "65f2e0404646022b005d622756ff24d71a263203eca96a17847b02358c1fb889",
  "cid": "QmV165f2e0404646022b005d622756ff24d71a263203",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293760,
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
      "evaluated_at": 1760293760
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
  "sig": "29554885bdd9ba5f832722e7dd38df927174905f0854cfefb5fd86c9eac86cb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025319716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 57534975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '46cae66c8ff70b91'}}}