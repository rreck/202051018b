```json
{
  "id": "4651832870fd5d97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290704,
  "host_pid": "9e6742732c60:1",
  "hash": "c975b9e9912fe188ac9d2d789bfcc6095b5381ac89dd55be8b8673b48d4cf4fe",
  "cid": "QmV1c975b9e9912fe188ac9d2d789bfcc6095b5381ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290704,
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
      "evaluated_at": 1760290704
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
  "sig": "bae26f23ff0fe4872e3200d739d477f9353ad21be82c7cd637b5a6bbc6d0b435"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 78034024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}