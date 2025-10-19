```json
{
  "id": "8d6dd004555a3581",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288061,
  "host_pid": "9e6742732c60:1",
  "hash": "8cb5b653470e03007f93c7984879d660225c9530640cbbe49fec5de1cc2fe600",
  "cid": "QmV18cb5b653470e03007f93c7984879d660225c9530",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288061,
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
      "evaluated_at": 1760288061
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
  "sig": "ec38dc0d6579fbe824650420e9b27fab6b66df1893691486602ecbefc95f6e51"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599118273
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 10526922, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': '777fe2ef7ab8cdc9'}}}