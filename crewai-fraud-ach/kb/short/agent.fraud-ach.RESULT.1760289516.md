```json
{
  "id": "3dccdfcdf981d413",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289516,
  "host_pid": "9e6742732c60:1",
  "hash": "81a23f1ef4808db7e0a84f60d9211aea8be6a516dae55eae569a6b3d3b830519",
  "cid": "QmV181a23f1ef4808db7e0a84f60d9211aea8be6a516",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289516,
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
      "evaluated_at": 1760289516
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "4aece4c8771d18ba99c94ab99babc5181bef113b5d0c2fab17d7aa9d092cd508"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 38867000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}