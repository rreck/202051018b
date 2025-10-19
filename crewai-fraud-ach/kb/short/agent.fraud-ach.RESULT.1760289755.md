```json
{
  "id": "dcba55da07f821d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289755,
  "host_pid": "9e6742732c60:1",
  "hash": "347b4cf1d418441dec51727c832f474bf56b06fe2aaecbce7ab95712674bba61",
  "cid": "QmV1347b4cf1d418441dec51727c832f474bf56b06fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289755,
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
      "evaluated_at": 1760289755
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
  "sig": "8c92567c58db1d1ecbe9c28aedec324cad621ac106b1bdf46c684d7448e8d725"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033554857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 63011124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}