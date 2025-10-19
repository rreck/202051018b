```json
{
  "id": "b26c383198f90405",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289543,
  "host_pid": "9e6742732c60:1",
  "hash": "9fda4dc3ce69af1580cf1fb47e452f634ac891c8d922eaaedf4ea5842b4350c8",
  "cid": "QmV19fda4dc3ce69af1580cf1fb47e452f634ac891c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289543,
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
      "evaluated_at": 1760289543
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
  "sig": "7feee6ced2d1225562be0f780f5929082a278c2f28ed9091b30ff968d7ddefc2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023553215
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 49341474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '85da211728f5a38f'}}}