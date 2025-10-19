```json
{
  "id": "d4b6ddca336ac3b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293363,
  "host_pid": "9e6742732c60:1",
  "hash": "45c5df5af5998775128d5510f7a6b98ba67b6e87b5745c4d84cf887936d21752",
  "cid": "QmV145c5df5af5998775128d5510f7a6b98ba67b6e87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293363,
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
      "evaluated_at": 1760293363
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
  "sig": "85eb5447cb330b46553059211322dc03f1946ed4d8db26af323c626367da923c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157190044
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 22615089, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '3b9549cbaaa9aa1e'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}