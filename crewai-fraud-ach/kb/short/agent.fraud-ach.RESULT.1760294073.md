```json
{
  "id": "5068008581894ffa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294073,
  "host_pid": "9e6742732c60:1",
  "hash": "57b7121e68af5eb4b362bca5bfed64379301d889f1a4ab68a8418c0908f9dbec",
  "cid": "QmV157b7121e68af5eb4b362bca5bfed64379301d889",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294073,
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
      "evaluated_at": 1760294073
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
  "sig": "abd9bd1c47a9eb8795a9ab9e2c1845cb30c2a3eefaccbd2b0bff0965f343e310"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461084458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 69749988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '14548b90fce01700'}}}