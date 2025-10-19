```json
{
  "id": "6805507057414dad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288110,
  "host_pid": "9e6742732c60:1",
  "hash": "46eb7aa03027ad9ffa27b2e282cc564536ec549990132bc9b51c5ffb7eb75879",
  "cid": "QmV146eb7aa03027ad9ffa27b2e282cc564536ec5499",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288110,
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
      "evaluated_at": 1760288110
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
  "sig": "dd9ce2397bce72f5cc25656374cf8b1ec70fa05cfcc5ed0054f83a23520ff831"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150168984
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 29932456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': '40857c0fb38af6a1'}}}