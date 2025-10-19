```json
{
  "id": "661435744c977742",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292403,
  "host_pid": "9e6742732c60:1",
  "hash": "50a6641a22162ccf02b17ee0c9666d9df8657619d4e6b819dcefeb1e856c5ad9",
  "cid": "QmV150a6641a22162ccf02b17ee0c9666d9df8657619",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292403,
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
      "evaluated_at": 1760292403
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
  "sig": "946b39ef85e792946357570a8cd1c79207e581584ab797954c5cf6d62d04e4bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270864889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 37451473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': 'c03eacc7eaf45e0d'}}}